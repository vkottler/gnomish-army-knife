-- https://wowprogramming.com/docs/api_categories.html
-- |cAARRGGBB

local project = "gnomish-army-knife"

-- Create UI menu.
local ui = createButtonContainer(UIParent, project, 2, 5)
ui:SetPoint("CENTER", UIParent, "CENTER", 0, 0)

-- Initially hidden.
ui:Hide()

-- Register mechanisms to show UI.
SLASH_GNOMISH_ARMY_KNIFE1 = "/" .. project
SLASH_GNOMISH_ARMY_KNIFE2 = "/gak"
SlashCmdList["GNOMISH_ARMY_KNIFE"] = function()
	if ui:IsShown() then
		ui:Hide()
	else
		ui:Show()
	end
end

-- Initialize application.
initHelpHarmBar(ui)
CVarManagementInit(ui)
KeybindManagementInit(ui)
MacroManagementInit(ui)
ActionBarManagementInit(ui)

-- Utility buttons.
createButton(ui, "Set UI", 0, 4, function()
	print("Set UI")
end)
createButton(ui, "Reload", 1, 4, function()
	ConsoleExec("reloadUI")
end)
