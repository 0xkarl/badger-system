from tqdm import tqdm
from brownie import *
from assistant.rewards.classes.RewardsList import RewardsList
from assistant.rewards.classes.RewardsLogger import rewardsLogger
from assistant.rewards.rewards_utils import get_latest_event_block,calc_meta_farm_rewards
from rich.console import Console
console = Console()
def calc_rewards(badger,start,end,nextCycle,events,name,token,retroactive,retroactiveStart):
    def filter_events(e):
        return int(e["blockNumber"]) > start and int(e["blockNumber"]) < end
    
    events = list(filter(filter_events,events))
    rewards = RewardsList(nextCycle,badger.badgerTree)
    if len(events) > 0:
        console.log("{} events to process for {}".format(len(events),name))
        startBlock = get_latest_event_block(events[0],events)
        if retroactive:
            startBlock = retroactiveStart 
        rewards = process_rewards(badger,startBlock,end,events,name,nextCycle,token)
    else:
        console.log("No events to process")
    return rewards


def process_rewards(badger,startBlock,endBlock,events,name,nextCycle,token):
    endBlock = int(events[0]["blockNumber"])
    totalFromEvents = sum([int(e["rewardAmount"]) for e in events])/1e18 
    rewards = RewardsList(nextCycle,badger.badgerTree)
    total = 0
    for i in tqdm(range(len(events))):
        event = events[i]
        userState = calc_meta_farm_rewards(badger,name,startBlock,endBlock)
        totalShareSeconds = sum([u.shareSeconds for u in userState])
        total += int(event["rewardAmount"])
        console.log("{} total {} processed".format(total/1e18,token))
        rewardsUnit = int(event["rewardAmount"])/totalShareSeconds
        for user in userState:
            rewards.increase_user_rewards(
                web3.toChecksumAddress(user.address),
                web3.toChecksumAddress(token),
                rewardsUnit * user.shareSeconds
            )
        rewardsLogger.add_user_share_seconds(user.address,name,user.shareSeconds)
        rewardsLogger.add_user_token(
            user.address,name,
            token,
            rewardsUnit * user.shareSeconds)

        if i+1 < len(events):
            startBlock = int(events[i]["blockNumber"])
            endBlock = int(events[i+1]["blockNumber"])

    totalFromRewards = sum([list(v.values())[0]/1e18 for v in list(rewards.claims.values()) ])

    # Calc diff of rewardsTotal and add assertion for checking rewards
    rewardsDiff = abs(totalFromRewards - totalFromRewards)* 1e18
    console.log("Total from Rewards: {} \nTotal from Events: {}\n Diff: {}".format(
        totalFromRewards,totalFromEvents,rewardsDiff
    ))
    if abs(totalFromEvents - totalFromRewards) > 100000:
        assert False, "Incorrect total rewards"

    distr = {}
    distr[token] = totalFromRewards
    rewardsLogger.add_distribution_info(name,distr)
    return rewards

    

