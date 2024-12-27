local buttonWidth = 120
local buttonHeight = 40
local headerHeight = 30
local padding = 10

function createButton(parent, text, xIndex, yIndex, method)
	local btn = CreateFrame("Button", nil, parent, "UIPanelButtonTemplate")

	-- Set dimensions.
	btn:SetSize(buttonWidth, buttonHeight)

	btn:SetPoint(
		"TOPLEFT",
		(btn:GetWidth() * xIndex) + padding,
		-headerHeight - (btn:GetHeight() * yIndex)
	)
	btn:SetText(text)
	btn:SetScript("OnClick", function(self, _, __)
		method()
	end)
	btn:RegisterForClicks("AnyDown")
end

function createButtonContainer(parent, text, width, height)
	local frame =
		CreateFrame("Frame", text, parent, "BasicFrameTemplateWithInset")

	-- Set dimensions.
	frame:SetSize(
		width * (buttonWidth + padding),
		headerHeight + (height * buttonHeight) + padding
	)

	-- Add a title.
	frame.TitleBg:SetHeight(30)
	frame.title = frame:CreateFontString(nil, "OVERLAY", "GameFontHighlight")
	frame.title:SetPoint("TOPLEFT", frame.TitleBg, "TOPLEFT", 5, -5)
	frame.title:SetText(text)

	-- Handle mouse move.
	-- https://wowpedia.fandom.com/wiki/Making_resizable_frames ?
	frame:EnableMouse(true)
	frame:SetMovable(true)
	frame:RegisterForDrag("LeftButton")
	frame:SetScript("OnDragStart", function(self)
		self:StartMoving()
	end)
	frame:SetScript("OnDragStop", function(self)
		self:StopMovingOrSizing()
	end)

	-- Handle show and hide.
	frame:SetScript("OnShow", function()
		PlaySound(808)
	end)
	frame:SetScript("OnHide", function()
		PlaySound(808)
	end)

	-- Register special frame.
	table.insert(UISpecialFrames, text)

	return frame
end
