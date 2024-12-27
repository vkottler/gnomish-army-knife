local function auditKeybinds()
	for i = 1, GetNumBindings() do
		command, category, key1, key2 = GetBinding(i, true)

		print(command, _G["BINDING_NAME_" .. command])

		if category then
			print("Category:", _G[category] or category)
		end

		if key1 then
			print("key1:", key1)
		end
		if key2 then
			print("key2:", key2)
		end
	end
end

local function setKeybinds()
	print("Set Keybinds")
end

function KeybindManagementInit(ui)
	createButton(ui, "Audit Keybinds", 0, 1, function()
		auditKeybinds()
	end)

	createButton(ui, "Set Keybinds", 1, 1, function()
		setKeybinds()
	end)
end
