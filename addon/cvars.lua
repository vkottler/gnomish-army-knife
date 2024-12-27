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
	createButton(ui, "Audit CVar's", 0, 0, function()
		print("Audit CVar's")
	end)

	createButton(ui, "Set CVar's", 1, 0, function()
		print("Set CVar's")
	end)
end
