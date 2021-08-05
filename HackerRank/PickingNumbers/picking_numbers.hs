allIndexPairs :: Int -> [(Int, Int)]
allIndexPairs s = [(i, j) | i <- [0..s - 2], j <- [i + 1..s - 1]]

allPairAbsDiffs :: [Int] -> [Int]
allPairAbsDiffs xs = map (\(i, j) -> abs $ xs !! i - xs !! j) $ allIndexPairs $ length xs

areDiffsInRange :: [Int] -> Bool
areDiffsInRange xs = all (<=1) $ allPairAbsDiffs xs

subarr :: [a] -> Int -> Int -> [a]
subarr xs i j = take (j - i + 1) $ drop i xs

findMaxSubarrLen :: [Int] -> Int
findMaxSubarrLen xs = maximum $ map checkValidity $ allIndexPairs $ length xs
    where checkValidity (i, j) = if (areDiffsInRange $ subarr xs i j) == True then j - i + 1 else 0

qsort :: (Ord a) => [a] -> [a]
qsort [] = []
qsort (x:xs) = left ++ [x] ++ right
    where left  = qsort [e | e <- xs, e <= x]
          right = qsort [e | e <- xs, e > x]

main = do
    getLine
    valsStr <- getLine
    let vals = map (read :: String -> Int) (words valsStr)
    print $ findMaxSubarrLen $ qsort vals