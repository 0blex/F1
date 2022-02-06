SELECT	r.raceid,
		r.year,
		r.round,
		r.name AS racename,
		r.date,
		r.circuitid,
		c.circuitref,
		c.name AS circuitname,
		c.location,
		c.country,
		c.alt AS altitude
FROM races r 
LEFT JOIN circuits c ON c.circuitid = r.circuitid
ORDER BY YEAR, ROUND