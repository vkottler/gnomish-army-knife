-- =====================================
-- generator=datazen
-- version=3.2.0
-- hash=f6f86b2cacec5562ad8db42630b25228
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
bindings["TARGETPARTYMEMBER1"] = { "PADFORWARD", nil }
bindings["TARGETPARTYMEMBER4"] = {
	"PADFORWARD",
	{
		"ALT",
	},
}
bindings["TARGETPARTYMEMBER2"] = {
	"PADFORWARD",
	{
		"SHIFT",
	},
}
bindings["TARGETPARTYMEMBER3"] = {
	"PADFORWARD",
	{
		"CTRL",
	},
}
bindings["TARGETSELF"] = {
	"PADFORWARD",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["TOGGLEGAK"] = {
	"PADFORWARD",
	{
		"ALT",
		"SHIFT",
	},
}
bindings["TOGGLEGAMEMENU"] = { "PADPADDLE4", nil }
bindings["TARGETARENA3"] = {
	"PADPADDLE4",
	{
		"ALT",
	},
}
bindings["TARGETARENA1"] = {
	"PADPADDLE4",
	{
		"SHIFT",
	},
}
bindings["TARGETARENA2"] = {
	"PADPADDLE4",
	{
		"CTRL",
	},
}
bindings["VEHICLEEXIT"] = {
	"PADPADDLE4",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["INTERACTTARGET"] = { "PADPADDLE3", nil }
bindings["MULTIACTIONBAR4BUTTON7"] = {
	"PADPADDLE3",
	{
		"ALT",
	},
}
bindings["MULTIACTIONBAR3BUTTON7"] = {
	"PADPADDLE3",
	{
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR4BUTTON1"] = {
	"PADPADDLE3",
	{
		"CTRL",
	},
}
bindings["EXTRAACTIONBUTTON1"] = {
	"PADPADDLE3",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["JUMP"] = { "PADPADDLE1", nil }
bindings["NEXTACTIONPAGE"] = {
	"PADPADDLE1",
	{
		"ALT",
	},
}
bindings["MULTIACTIONBAR3BUTTON8"] = {
	"PADPADDLE1",
	{
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR4BUTTON2"] = {
	"PADPADDLE1",
	{
		"CTRL",
	},
}
bindings["MULTIACTIONBAR4BUTTON8"] = {
	"PADPADDLE1",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["TOGGLEWORLDMAP"] = { "PADBACK", nil }
bindings["TOGGLECHARACTER0"] = {
	"PADBACK",
	{
		"ALT",
	},
}
bindings["TOGGLESPELLBOOK"] = {
	"PADBACK",
	{
		"SHIFT",
	},
}
bindings["TOGGLETALENTS"] = {
	"PADBACK",
	{
		"CTRL",
	},
}
bindings["TOGGLEACHIEVEMENT"] = {
	"PADBACK",
	{
		"ALT",
		"SHIFT",
	},
}
bindings["OPENALLBAGS"] = {
	"PADBACK",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["TOGGLECOLLECTIONS"] = {
	"PADBACK",
	{
		"ALT",
		"CTRL",
	},
}
bindings["TOGGLEAUTORUN"] = { "PADSYSTEM", nil }
bindings["TOGGLEGROUPFINDER"] = {
	"PADSYSTEM",
	{
		"ALT",
	},
}
bindings["TOGGLEPROFESSIONBOOK"] = {
	"PADSYSTEM",
	{
		"SHIFT",
	},
}
bindings["TOGGLEENCOUNTERJOURNAL"] = {
	"PADSYSTEM",
	{
		"CTRL",
	},
}
bindings["TOGGLEGUILDTAB"] = {
	"PADSYSTEM",
	{
		"ALT",
		"SHIFT",
	},
}
bindings["FOLLOWTARGET"] = {
	"PADSYSTEM",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["TOGGLEWORLDSTATESCORES"] = {
	"PADSYSTEM",
	{
		"ALT",
		"CTRL",
	},
}
bindings["ACTIONBUTTON1"] = { "PADRSHOULDER", nil }
bindings["MULTIACTIONBAR2BUTTON7"] = {
	"PADRSHOULDER",
	{
		"ALT",
	},
}
bindings["ACTIONBUTTON7"] = {
	"PADRSHOULDER",
	{
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR1BUTTON1"] = {
	"PADRSHOULDER",
	{
		"CTRL",
	},
}
bindings["MULTIACTIONBAR3BUTTON1"] = {
	"PADRSHOULDER",
	{
		"ALT",
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR1BUTTON7"] = {
	"PADRSHOULDER",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR2BUTTON1"] = {
	"PADRSHOULDER",
	{
		"ALT",
		"CTRL",
	},
}
bindings["ACTIONBUTTON2"] = { "PADRTRIGGER", nil }
bindings["MULTIACTIONBAR2BUTTON8"] = {
	"PADRTRIGGER",
	{
		"ALT",
	},
}
bindings["ACTIONBUTTON8"] = {
	"PADRTRIGGER",
	{
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR1BUTTON2"] = {
	"PADRTRIGGER",
	{
		"CTRL",
	},
}
bindings["MULTIACTIONBAR3BUTTON2"] = {
	"PADRTRIGGER",
	{
		"ALT",
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR1BUTTON8"] = {
	"PADRTRIGGER",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR2BUTTON2"] = {
	"PADRTRIGGER",
	{
		"ALT",
		"CTRL",
	},
}
bindings["ACTIONBUTTON3"] = { "PAD3", nil }
bindings["MULTIACTIONBAR2BUTTON9"] = {
	"PAD3",
	{
		"ALT",
	},
}
bindings["ACTIONBUTTON9"] = {
	"PAD3",
	{
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR1BUTTON3"] = {
	"PAD3",
	{
		"CTRL",
	},
}
bindings["MULTIACTIONBAR3BUTTON3"] = {
	"PAD3",
	{
		"ALT",
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR1BUTTON9"] = {
	"PAD3",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR2BUTTON3"] = {
	"PAD3",
	{
		"ALT",
		"CTRL",
	},
}
bindings["ACTIONBUTTON4"] = { "PAD1", nil }
bindings["MULTIACTIONBAR2BUTTON10"] = {
	"PAD1",
	{
		"ALT",
	},
}
bindings["ACTIONBUTTON10"] = {
	"PAD1",
	{
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR1BUTTON4"] = {
	"PAD1",
	{
		"CTRL",
	},
}
bindings["MULTIACTIONBAR3BUTTON4"] = {
	"PAD1",
	{
		"ALT",
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR1BUTTON10"] = {
	"PAD1",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR2BUTTON4"] = {
	"PAD1",
	{
		"ALT",
		"CTRL",
	},
}
bindings["ACTIONBUTTON5"] = { "PAD4", nil }
bindings["MULTIACTIONBAR2BUTTON11"] = {
	"PAD4",
	{
		"ALT",
	},
}
bindings["ACTIONBUTTON11"] = {
	"PAD4",
	{
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR1BUTTON5"] = {
	"PAD4",
	{
		"CTRL",
	},
}
bindings["MULTIACTIONBAR3BUTTON5"] = {
	"PAD4",
	{
		"ALT",
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR1BUTTON11"] = {
	"PAD4",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR2BUTTON5"] = {
	"PAD4",
	{
		"ALT",
		"CTRL",
	},
}
bindings["ACTIONBUTTON6"] = { "PAD2", nil }
bindings["MULTIACTIONBAR2BUTTON12"] = {
	"PAD2",
	{
		"ALT",
	},
}
bindings["ACTIONBUTTON12"] = {
	"PAD2",
	{
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR1BUTTON6"] = {
	"PAD2",
	{
		"CTRL",
	},
}
bindings["MULTIACTIONBAR3BUTTON6"] = {
	"PAD2",
	{
		"ALT",
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR1BUTTON12"] = {
	"PAD2",
	{
		"CTRL",
		"SHIFT",
	},
}
bindings["MULTIACTIONBAR2BUTTON6"] = {
	"PAD2",
	{
		"ALT",
		"CTRL",
	},
}
