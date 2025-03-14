# Copyright 2023 invoker__qq. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import sys
import os

# 动态添加路径
for root, dirs, files in os.walk('.'):
    sys.path.append(root)

# 导入游戏包装器
from FinalMissionWrapper import FinalMission
from RushnAttackWrapper import RushnAttack
from SuperMarioBrosWrapper import SuperMarioBros
from ninja_turtles_fight_wrapper import TeenageMutantNinjaTurtlesTournamentFighters

# 游戏映射
game_mapping = {
    "1": {"wrapper": SuperMarioBros, "game": "SuperMarioBros-Nes", "state": "Level1-1"},
    "2": {"wrapper": TeenageMutantNinjaTurtlesTournamentFighters, "game": "TeenageMutantNinjaTurtlesTournamentFighters-Nes", "state": "Level1.LeoVsRaph.Tournament"},
    "3": {"wrapper": FinalMission, "game": "SCATSpecialCyberneticAttackTeam-Nes", "state": "1Player.Level1"},
    "4": {"wrapper": RushnAttack, "game": "RushnAttack-Nes", "state": "1Player.Level1"}
}

def get_game_info(game_number):
    """根据游戏编号获取游戏信息"""
    game_info = game_mapping.get(game_number)

    if game_info is None:
        print(f"Invalid game number. Please choose from {', '.join(game_mapping.keys())}.")
        sys.exit(1)

    return game_info