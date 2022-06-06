SELECT
	RE.resultID,
	RA.year,
	RE.raceID,
	RA.round,
	RA.name AS raceName,
	RA.circuitID,
	CI.circuitRef,
	CI.name AS circuitName,
	CI.country,
	Ci.alt AS altitude,
	RE.driverID,
	D.code AS DriverCode,
	D.driverRef,
	D.forename+' '+D.surname AS driverName,
	RE.constructorID,
	CO.constructorRef,
	CO.name AS constructorName,
	RE.grid AS gridPosition,
	RE.position AS racePosition,
	RE.positionText AS RacePositionText,
	CAST(RE.points AS DECIMAL(3,1)) AS points
FROM results RE
JOIN races RA ON RE.raceid = RA.raceID
JOIN circuits CI ON RA.circuitID = CI.circuitID
JOIN constructors CO ON CO.constructorID = RE.constructorID
JOIN drivers D ON D.driverID = RE.driverID
ORDER BY year, round, raceposition

