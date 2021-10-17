splitHalves :: [a] -> ([a], [a])
splitHalves xs = (left, right)
    where left    = take halfLen xs
          right   = drop halfLen xs
          halfLen = floor $ fromIntegral (length xs) / 2

merge :: (Ord a) => [a] -> [a] -> [a]
merge [] []     = []
merge (x:xs) [] = x:merge xs []
merge [] (y:ys) = y:merge [] ys
merge (x:xs) (y:ys)
    | x <= y    = x:merge xs (y:ys)
    | otherwise = y:merge (x:xs) ys

invCount :: (Ord a) => [a] -> Int
invCount [] = 0
invCount [x] = 0
invCount xs = 1

mergeSort :: (Ord a) => [a] -> [a]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort xs = merge left' right'
    where (left, right) = splitHalves xs
          left'         = mergeSort left
          right'        = mergeSort right
