USE F1
SELECT * 
FROM results res
	LEFT JOIN 
	INNER JOIN races ra ON res.raceid = ra.raceid
	INNER JOIN drivers d ON res.driverid = d.driverid
	INNER JOIN constructors c ON res.constructorid = c.constructorid
	INNER JOIN qualifying q ON q.raceid=res.raceid AND q.driverid=res.driverid
	


SELECT * 
FROM qualifying Q
INNER JOIN results R ON Q.raceid=R.raceid AND Q.driverid = R.driverid


SELECT *
FROM status