SELECT	r.raceid,
		r.year,
		r.round,
		r.name AS raceName,
		r.date,
		r.circuitID,
		c.circuitRef,
		c.name AS circuitName,
		c.location,
		c.country,
		c.lat AS latitude,
		c.lng AS longitude,
		c.alt AS altitude
FROM races r 
LEFT JOIN circuits c ON c.circuitid = r.circuitid
ORDER BY YEAR, ROUND