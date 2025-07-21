import discord
from discord import ui, Interaction

class PanelButtonView(ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot

    # ✅ 通知の予約ボタン
    @ui.button(label="🔔 通知の予約", style=discord.ButtonStyle.primary, custom_id="panel_notify")
    async def notify_button(self, interaction: Interaction, button: ui.Button):
        await interaction.response.send_message("🔧 通知の予約を開始します（※処理は未実装）", ephemeral=True)

    # ✅ 通知の確認・編集・削除
    @ui.button(label="📋 通知の確認・編集・削除", style=discord.ButtonStyle.secondary, custom_id="panel_check_edit")
    async def check_edit_button(self, interaction: Interaction, button: ui.Button):
        await interaction.response.send_message("📋 予約された通知を確認します（※処理は未実装）", ephemeral=True)

    # ✅ ランダム数（1つ選ぶ）
    @ui.button(label="🎯 数字を1つ選ぶ", style=discord.ButtonStyle.success, custom_id="panel_pick1")
    async def pick_one(self, interaction: Interaction, button: ui.Button):
        await interaction.response.send_message("🎲 ランダムで1つの数字を選びます（※処理は未実装）", ephemeral=True)

    # ✅ ランダム数（2つ選ぶ）
    @ui.button(label="🎯 数字を2つ選ぶ", style=discord.ButtonStyle.success, custom_id="panel_pick2")
    async def pick_two(self, interaction: Interaction, button: ui.Button):
        await interaction.response.send_message("🎲 ランダムで2つの数字を選びます（※処理は未実装）", ephemeral=True)

    # ✅ @everyone 呼び出し系（仮）
    @ui.button(label="📣 財宝", style=discord.ButtonStyle.danger, custom_id="call_treasure")
    async def call_treasure(self, interaction: Interaction, button: ui.Button):
        await interaction.response.send_message("@everyone 財宝イベントの呼び出し（※未実装）", ephemeral=True)

    @ui.button(label="📣 軍事演習", style=discord.ButtonStyle.danger, custom_id="call_military")
    async def call_military(self, interaction: Interaction, button: ui.Button):
        await interaction.response.send_message("@everyone 軍事演習の呼び出し（※未実装）", ephemeral=True)

    @ui.button(label="📣 ゾンビ侵攻", style=discord.ButtonStyle.danger, custom_id="call_zombie")
    async def call_zombie(self, interaction: Interaction, button: ui.Button):
        await interaction.response.send_message("@everyone ゾンビ侵攻の呼び出し（※未実装）", ephemeral=True)

    @ui.button(label="📣 バリア", style=discord.ButtonStyle.danger, custom_id="call_barrier")
    async def call_barrier(self, interaction: Interaction, button: ui.Button):
        await interaction.response.send_message("@everyone バリア準備の呼び出し（※未実装）", ephemeral=True)

    @ui.button(label="📣 臨戦態勢", style=discord.ButtonStyle.danger, custom_id="call_battle")
    async def call_battle(self, interaction: Interaction, button: ui.Button):
        await interaction.response.send_message("@everyone 臨戦態勢の呼び出し（※未実装）", ephemeral=True)
