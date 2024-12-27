-- make an auto-generated metadata lua file so we can source these vars

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
function CVarManagementInit(ui)
	local btn = CreateFrame("Button", nil, ui, "UIPanelButtonTemplate")
	btn:SetPoint("CENTER")
	btn:SetSize(100, 40)
	btn:SetText("Click me")
	btn:SetScript("OnClick", function(self, button, down)
		print("Pressed", button, down and "down" or "up")
	end)
	btn:RegisterForClicks("AnyDown", "AnyUp")

	print("Initialized CVar management.")
end
