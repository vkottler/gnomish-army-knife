function table_contains(tbl, x)
	found = false
	for _, v in pairs(tbl) do
		if v == x then
			found = true
		end
	end
	return found
end

local function checkCommand(command, fix)
	if bindings[command] then
		local gamepad = bindings[command][1]
		local key = keymap[gamepad]

		gamepad_parts = {}
		key_parts = {}
		if bindings[command][2] then
			for _, val in pairs(bindings[command][2]) do
				table.insert(gamepad_parts, val)
				table.insert(key_parts, val)
			end
		end
		table.insert(gamepad_parts, gamepad)
		table.insert(key_parts, key)

		local gamepad_str = table.concat(gamepad_parts, "-")
		local key_str = table.concat(key_parts, "-")

		-- https://wowwiki-archive.fandom.com/wiki/API_GetBindingKey
		bound = { GetBindingKey(command) }

		if not table_contains(bound, gamepad_str) then
			if fix then
				if SetBinding(gamepad_str, command) then
					print(gamepad_str, "->", command, "success")
				else
					print(gamepad_str, "->", command, "fail")
				end
			else
				print(gamepad_str, "not bound to", command, "!")
			end
		end
		if not table_contains(bound, key_str) then
			if fix then
				if SetBinding(key_str, command) then
					print(key_str, "->", command, "success")
				else
					print(key_str, "->", command, "fail")
				end
			else
				print(key_str, "not bound to", command, "!")
			end
		end
	else
		print("No binding for command", command, "!")
	end
end

local function auditKeybinds()
	-- Audit command bindings.
	for command, _ in pairs(bindings) do
		checkCommand(command, false)
	end

	-- for i = 1, GetNumBindings() do
	-- command, category, key1, key2 = GetBinding(i, true)
	-- _G["BINDING_NAME_" .. command]
	-- _G[category]
	-- if string.find(command, "LUA") then
	-- 	print(command)
	-- end
	-- local search = "PAD4"
	-- if key1 and string.find(key1, search) then
	-- 	print(command, key1, key2)
	-- end
	-- if key2 and string.find(key2, search) then
	-- 	print(command, key1, key2)
	-- end
	-- end
end

local function setKeybinds()
	-- Fix command bindings.
	for command, _ in pairs(bindings) do
		checkCommand(command, true)
	end

	SaveBindings(1)
end

function KeybindManagementInit(ui)
	createButton(ui, "Audit Keybinds", 0, 1, function()
		auditKeybinds()
	end)

	createButton(ui, "Set Keybinds", 1, 1, function()
		setKeybinds()
	end)
end
