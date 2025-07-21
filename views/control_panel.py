import discord
from discord import ui, Interaction

class ControlPanelView(ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        # 通知関連
        self.add_item(ui.Button(label="📝 通知を予約", style=discord.ButtonStyle.primary, custom_id="reserve_notify"))
        self.add_item(ui.Button(label="📋 通知の確認・編集・削除", style=discord.ButtonStyle.secondary, custom_id="manage_notify"))

        # ランダムピック
        self.add_item(ui.Button(label="🎯 1つ選ぶ", style=discord.ButtonStyle.success, custom_id="pick_one"))
        self.add_item(ui.Button(label="🎯 2つ選ぶ", style=discord.ButtonStyle.success, custom_id="pick_two"))

        # @everyone 呼び出しボタン群
        self.add_item(ui.Button(label="💰 財宝", style=discord.ButtonStyle.danger, custom_id="call_treasure"))
        self.add_item(ui.Button(label="🛡️ 軍事演習", style=discord.ButtonStyle.danger, custom_id="call_drill"))
        self.add_item(ui.Button(label="🧟 ゾンビ侵攻", style=discord.ButtonStyle.danger, custom_id="call_zombie"))
        self.add_item(ui.Button(label="🌀 バリア", style=discord.ButtonStyle.danger, custom_id="call_barrier"))
        self.add_item(ui.Button(label="⚔️ 臨戦態勢", style=discord.ButtonStyle.danger, custom_id="call_battle"))

    async def interaction_check(self, interaction: Interaction) -> bool:
        # 任意のユーザー制限などを後で追加可能
        return True
