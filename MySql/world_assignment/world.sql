SELECT countries.name, languages.language, 
languages.percentage 
FROM languages
JOIN countries
ON languages.country_id = countries.id
WHERE language = 'Slovene'
ORDER BY languages.percentage DESC;

SELECT countries.name AS "Country", COUNT(cities.name) AS "# of Cities"
FROM countries
JOIN cities
ON countries.id = cities.country_id

;

SELECT countries.name AS "Country", cities.name AS "# of Cities"
FROM countries
JOIN cities
ON countries.id = cities.country_id
;

SELECT cities.name, cities.population
FROM cities
JOIN countries
ON cities.country_id = countries.id
WHERE countries.name= "Mexico"
HAVING cities.population>500000
ORDER BY cities.population DESC
;







