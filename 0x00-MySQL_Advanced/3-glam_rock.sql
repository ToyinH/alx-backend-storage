-- old school band
SELECT 
    band_name,
    CASE 
        WHEN split IS NOT NULL THEN YEAR(split) - YEAR(formed)
        ELSE 2022 - YEAR(formed)
    END AS lifespan
FROM 
    metal_bands
WHERE 
    style = 'Glam rock'
ORDER BY 
    lifespan DESC;
