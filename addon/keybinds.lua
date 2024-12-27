function KeybindManagementInit(ui)
	createButton(ui, "Audit Keybinds", 0, 1, function()
		print("Audit Keybinds")
	end)

	createButton(ui, "Set Keybinds", 1, 1, function()
		print("Set Keybinds")
	end)
end
