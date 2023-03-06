from __future__ import annotations

from gradio.themes.base import Base
from gradio.themes.utils import colors, sizes


class Glass(Base):
    def __init__(
        self,
        *,
        hue: colors.Color | str = colors.stone,
        spacing_size: sizes.Size | str = sizes.spacing_sm,
        radius_size: sizes.Size | str = sizes.radius_sm,
        text_size: sizes.Size | str = sizes.text_sm,
    ):
        super().__init__(
            primary_hue=hue,
            secondary_hue=hue,
            neutral_hue=hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
        )
        super().set(
            body_background_color_dark="*primary_800",
            color_background_secondary_dark="*primary_800",
            block_background_dark="*primary_800",
            button_primary_background="linear-gradient(180deg, *primary_50 0%, *primary_200 50%, *primary_300 50%, *primary_200 100%)",
            button_primary_background_hover="linear-gradient(180deg, *primary_100 0%, *primary_200 50%, *primary_300 50%, *primary_200 100%)",
            button_primary_background_dark="linear-gradient(180deg, *primary_400 0%, *primary_500 50%, *primary_600 50%, *primary_500 100%)",
            button_primary_background_hover_dark="linear-gradient(180deg, *primary_400 0%, *primary_500 50%, *primary_600 50%, *primary_500 100%)",
            button_secondary_background="*button_primary_background",
            button_secondary_background_hover="*button_primary_background_hover",
            button_secondary_background_dark="*button_primary_background",
            button_secondary_background_hover_dark="*button_primary_background_hover",
            button_cancel_background="*button_primary_background",
            button_cancel_background_hover="*button_primary_background_hover",
            button_cancel_background_dark="*button_primary_background",
            button_cancel_background_hover_dark="*button_primary_background_hover",
            button_cancel_border_color="*button_secondary_border_color",
            button_cancel_border_color_dark="*button_secondary_border_color",
            button_cancel_text_color="*button_secondary_text_color",
            checkbox_border_width="0px",
            checkbox_label_background="*button_secondary_background",
            checkbox_label_background_dark="*button_secondary_background",
            checkbox_label_background_hover="*button_secondary_background_hover",
            checkbox_label_background_hover_dark="*button_secondary_background_hover",
            checkbox_label_border_width="1px",
            checkbox_background_dark="*primary_600",
            button_border_width="1px",
            button_shadow_active="*shadow_inset",
            input_background="linear-gradient(0deg, *secondary_50 0%, white 100%)",
            input_background_dark="*secondary_600",
            input_border_width="1px",
            slider_color="*primary_400",
            block_label_color="*primary_500",
            block_title_color="*primary_500",
            block_label_text_weight="600",
            block_title_text_weight="600",
            block_label_text_size="*text_md",
            block_title_text_size="*text_md",
            block_label_background="*primary_200",
            block_label_background_dark="*primary_700",
            block_border_width="0px",
            block_border_width_dark="1px",
            panel_border_width="1px",
            color_border_primary_dark="*primary_500",
            color_background_primary_dark="*neutral_700",
            color_background_secondary="*primary_100",
            block_background="*primary_50",
            block_shadow="*primary_400 0px 0px 3px 0px",
            table_even_background_dark="*neutral_700",
            table_odd_background_dark="*neutral_700",
        )
