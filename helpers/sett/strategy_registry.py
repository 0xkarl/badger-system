from brownie import *

name_to_artifact = {
    "SmartVesting": SmartVesting,
    "SmartTimelock": SmartTimelock,
    "RewardsEscrow": RewardsEscrow,
    "BadgerGeyser": BadgerGeyser,
    "BadgerTree": BadgerTree,
    "BadgerHunt": BadgerHunt,
    "SimpleTimelock": SimpleTimelock,
    "Controller": Controller,
    "Sett": Sett,
    "SettV1": Sett,
    "SettV1.1": Sett,
    "StakingRewards": StakingRewards,
    "StakingRewardsSignalOnly": StakingRewardsSignalOnly,
    "StrategyBadgerRewards": StrategyBadgerRewards,
    "StrategyBadgerLpMetaFarm": StrategyBadgerLpMetaFarm,
    "StrategyHarvestMetaFarm": StrategyHarvestMetaFarm,
    "StrategyPickleMetaFarm": StrategyPickleMetaFarm,
    "StrategyCurveGaugeTbtcCrv": StrategyCurveGaugeTbtcCrv,
    "StrategyCurveGaugeSbtcCrv": StrategyCurveGaugeSbtcCrv,
    "StrategyCurveGaugeRenBtcCrv": StrategyCurveGaugeRenBtcCrv,
    "StrategySushiBadgerWbtc": StrategySushiBadgerWbtc,
    "StrategySushiLpOptimizer": StrategySushiLpOptimizer,
    "StrategyDiggRewards": StrategyDiggRewards,
    "StrategyDiggLpMetaFarm": StrategyDiggLpMetaFarm,
    "StrategySushiDiggWbtcLpOptimizer": StrategySushiDiggWbtcLpOptimizer,
    "DiggRewardsFaucet": DiggRewardsFaucet,
    "DiggSett": DiggSett,
    "HoneypotMeme": HoneypotMeme,
    "UFragments": UFragments,
    "UFragmentsPolicy": UFragmentsPolicy,
    "SimpleTimelock": SimpleTimelock,
    "SmartVesting": SmartVesting,
    "DiggDistributor": DiggDistributor
}


def strategy_name_to_artifact(name):
    return name_to_artifact[name]
