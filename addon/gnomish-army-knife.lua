-- https://wowprogramming.com/docs/api_categories.html
-- |cAARRGGBB

local project = "gnomish-army-knife"

-- Create UI menu.
local ui =
	CreateFrame("Frame", project, UIParent, "BasicFrameTemplateWithInset")
ui:SetSize(400, 300)
ui:SetPoint("CENTER", UIParent, "CENTER", 0, 0)

-- Initially hidden.
ui:Hide()

-- Add a title.
ui.TitleBg:SetHeight(30)
ui.title = ui:CreateFontString(nil, "OVERLAY", "GameFontHighlight")
ui.title:SetPoint("TOPLEFT", ui.TitleBg, "TOPLEFT", 5, -5)
ui.title:SetText(project)

-- Handle mouse move.
-- https://wowpedia.fandom.com/wiki/Making_resizable_frames ?
ui:EnableMouse(true)
ui:SetMovable(true)
ui:RegisterForDrag("LeftButton")
ui:SetScript("OnDragStart", function(self)
	self:StartMoving()
end)
ui:SetScript("OnDragStop", function(self)
	self:StopMovingOrSizing()
end)

-- Handle show and hide.
ui:SetScript("OnShow", function()
	PlaySound(808)
end)
ui:SetScript("OnHide", function()
	PlaySound(808)
end)

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

-- Register special frame.
table.insert(UISpecialFrames, project)

-- Initialize application.
initHelpHarmBar(ui)
CVarManagementInit(ui)
KeybindManagementInit(ui)
