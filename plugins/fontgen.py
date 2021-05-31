"""
{i}
"""

from . import _default, _double_stroke, script_royal, _monospace, _small_caps

fonts = ["small caps ", "monospace ", "double stroke ", "script royal"]


@ultroid_cmd(
    pattern="font ?(.*)",
)
async def _(e):
    input = e.pattern_match.group(1)
    try:
        font = input.split(":", maxsplit=1)[0]
        text = input.split(":", maxsplit=1)[1]
    except BaseException:
        pass  # todo
    if font not in fonts:
        return  # todo
    if font == "small caps ":
        msg = gen_font(text, _small_caps)
    if font == "monospace ":
        msg = gen_font(text, _monospace)
    if font == "double stroke ":
        msg = gen_font(text, _double_stroke)
    if font == "script royal ":
        msg = gen_font(text, _script_royal)
    await eor(e, msg)
    # todo tmrw


def gen_font(text, new_font):
    for q in text:
        if q in _default:
            new = new_font[_default.index(q)]
            text = text.replace(q, new)
    return text
