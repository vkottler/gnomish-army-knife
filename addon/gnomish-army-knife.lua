-- https://wowprogramming.com/docs/api_categories.html
-- |cAARRGGBB

-- info = {C_CVar.GetCVarInfo("GamePadEnable")}
-- print(info[1])

-- CVar's to set/audit
-- ----------------------------------------------------------------------------
-- GamePadEnable 1

-- https://wowpedia.fandom.com/wiki/Game_Pad_buttons
-- GamePadEmulateAlt PADPADDLE2

-- GamePadRunThreshold 0
-- GamePadCameraYawSpeed 1.75
-- advancedCombatLogging 1
-- ----------------------------------------------------------------------------

-- https://wowpedia.fandom.com/wiki/Events
-- ACTIONBAR_PAGE_CHANGED
local function initHelpHarmBar()
	-- need some kind of actual UI interaction, attempt to replace the "1"
	-- and "2" elements? or is that not possible
	-- https://wowpedia.fandom.com/wiki/UIOBJECT_Frame
	local frame = CreateFrame("Frame")

	-- check if current bar is "1" or "2" to initialize properly
	-- GetActionBarPage()

	-- https://wowpedia.fandom.com/wiki/UIHANDLER_OnEvent
	frame:SetScript("OnEvent", function(_, event)
		if event == "ACTIONBAR_PAGE_CHANGED" then
			message("current action bar: " .. GetActionBarPage())
		end
	end)
	frame:RegisterEvent("ACTIONBAR_PAGE_CHANGED")
end

local function main()
	initHelpHarmBar()
end

main()
