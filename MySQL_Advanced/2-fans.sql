-- Script selects origin and fans columns in
-- metal_bands table and sorts them by num of fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
