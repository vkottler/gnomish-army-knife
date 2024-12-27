local function doesCVarMatch(key, log)
	info = { C_CVar.GetCVarInfo(key) }

	-- Convert strings to numbers for comparison if necessary.
	local toCompare = info[1]
	local val = expectedCVars[key]
	if type(val) == "number" then
		toCompare = tonumber(toCompare)
	end

	local result = val == toCompare

	if not result and log then
		print(key, "doesn't match!", val, "!=", toCompare)
	end

	return result
end

local function auditCVars()
	local visited = {}
	local matchCount = 0

	for key, val in pairs(expectedCVars) do
		if doesCVarMatch(key, true) then
			matchCount = matchCount + 1
		end
		table.insert(visited, key)
	end

	print(matchCount, "/", table.getn(visited), "variables match.")
end

local function setCVars()
	for key, val in pairs(expectedCVars) do
		if not doesCVarMatch(key, false) then
			if C_CVar.SetCVar(key, val) then
				print("Set", key, "to", val)
			else
				print("Failed to set", key, "to", val)
			end
		end
	end
end

function CVarManagementInit(ui)
	createButton(ui, "Audit CVar's", 0, 0, function()
		auditCVars()
	end)

	createButton(ui, "Set CVar's", 1, 0, function()
		setCVars()
	end)
end
