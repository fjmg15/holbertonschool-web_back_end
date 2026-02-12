-- Script sorts bands in desc order of
-- life span
SELECT band_name, IFNULL(split, 2025) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
