-- =====================================
-- generator=datazen
-- version=3.2.0
-- hash=c868d2af5ac12db5e06e4da5224c5fca
-- =====================================
-- Mapping of gamepad inputs to keyboard inputs.
keymap = {}
keymap["PADRTRIGGER"] = "BUTTON4"
keymap["PADRSHOULDER"] = "BUTTON5"
keymap["PAD1"] = "S"
keymap["PAD2"] = "R"
keymap["PAD3"] = "Q"
keymap["PAD4"] = "3"
keymap["PADDLEFT"] = "2"
keymap["PADDUP"] = "MOUSEWHEELUP"
keymap["PADDDOWN"] = "MOUSEWHEELDOWN"
keymap["PADDRIGHT"] = "4"
keymap["PADLSTICK"] = "T"
keymap["PADRSTICK"] = "V"
keymap["PADBACK"] = "Z"
keymap["PADSYSTEM"] = "X"
keymap["PADFORWARD"] = "C"
keymap["PADPADDLE1"] = "SPACE"
keymap["PADPADDLE2"] = "ALT"
keymap["PADPADDLE3"] = "F"
keymap["PADPADDLE4"] = "1"

-- Mapping of gamepad inputs to command plus any modifiers.
bindings = {}
bindings["TARGETFOCUS"] = { "PADDLEFT", nil }
bindings["MULTIACTIONBAR4BUTTON9"] = {
	"PADDLEFT",
	{
		"ALT",
	},
}
bindings["MULTIACTIONBAR3BUTTON9"] = {
	"PADDLEFT",
	{
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR4BUTTON3"] = {
	"PADDLEFT",
	{
		"CTRL",
	},
}
bindings["FOCUSTARGET"] = {
	"PADDLEFT",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["TARGETNEARESTFRIENDPLAYER"] = { "PADDDOWN", nil }
bindings["MULTIACTIONBAR4BUTTON10"] = {
	"PADDDOWN",
	{
		"ALT",
	},
}
bindings["MULTIACTIONBAR3BUTTON10"] = {
	"PADDDOWN",
	{
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR4BUTTON4"] = {
	"PADDDOWN",
	{
		"CTRL",
	},
}
bindings["TARGETPREVIOUSFRIENDPLAYER"] = {
	"PADDDOWN",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["TARGETNEARESTENEMYPLAYER"] = { "PADDUP", nil }
bindings["MULTIACTIONBAR4BUTTON11"] = {
	"PADDUP",
	{
		"ALT",
	},
}
bindings["MULTIACTIONBAR3BUTTON11"] = {
	"PADDUP",
	{
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR4BUTTON5"] = {
	"PADDUP",
	{
		"CTRL",
	},
}
bindings["TARGETNEARESTENEMY"] = {
	"PADDUP",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["TARGETSCANENEMY"] = {
	"PADDUP",
	{
		"ALT",
		"SHIFT",
	},
}
bindings["ASSISTTARGET"] = { "PADDRIGHT", nil }
bindings["MULTIACTIONBAR4BUTTON12"] = {
	"PADDRIGHT",
	{
		"ALT",
	},
}
bindings["MULTIACTIONBAR3BUTTON12"] = {
	"PADDRIGHT",
	{
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR4BUTTON6"] = {
	"PADDRIGHT",
	{
		"CTRL",
	},
}
bindings["TARGETLASTTARGET"] = {
	"PADDRIGHT",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["FRIENDNAMEPLATES"] = { "PADLSTICK", nil }
bindings["NAMEPLATES"] = { "PADRSTICK", nil }
bindings["TOGGLE_VOICE_SELF_MUTE"] = {
	"PADLSTICK",
	{
		"ALT",
	},
}
bindings["TOGGLE_VOICE_SELF_DEAFEN"] = {
	"PADRSTICK",
	{
		"ALT",
	},
}
bindings["CAMERAZOOMOUT"] = {
	"PADLSTICK",
	{
		"SHIFT",
	},
}
bindings["CAMERAZOOMIN"] = {
	"PADRSTICK",
	{
		"SHIFT",
	},
}
bindings["TOGGLESHEATH"] = {
	"PADLSTICK",
	{
		"CTRL",
	},
}
bindings["TOGGLEFPS"] = {
	"PADRSTICK",
	{
		"CTRL",
	},
}
bindings["FLIPCAMERAYAW"] = {
	"PADLSTICK",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["CENTERCAMERA"] = {
	"PADRSTICK",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["TOGGLEUI"] = {
	"PADLSTICK",
	{
		"ALT",
		"SHIFT",
	},
}
bindings["SCREENSHOT"] = {
	"PADRSTICK",
	{
		"ALT",
		"SHIFT",
	},
}
