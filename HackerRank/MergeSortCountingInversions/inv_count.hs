import Control.Monad

splitHalves :: [a] -> ([a], [a])
splitHalves xs = (left, right)
    where left    = take halfLen xs
          right   = drop halfLen xs
          halfLen = floor $ fromIntegral (length xs) / 2

mergeCountInv :: (Ord a) => [a] -> [a] -> ([a], Int)
mergeCountInv [] [] = ([], 0)
mergeCountInv xs [] = (xs, 0)
mergeCountInv [] ys = (ys, 0)
mergeCountInv (x:xs) (y:ys)
    | x <= y    = (x:xs', invLeft)
    | otherwise = (y:ys', invRight + length xs + 1)
    where (xs', invLeft)  = mergeCountInv xs (y:ys)
          (ys', invRight) = mergeCountInv (x:xs) ys

invCount :: (Ord a) => [a] -> Int
invCount [] = 0
invCount [x] = 0
invCount xs = invLeft + invRight + invBoth
    where (left, right) = splitHalves xs
          invLeft       = invCount left
          invRight      = invCount right
          (_, invBoth)  = mergeCountInv left right

processTestCase :: Int -> IO()
processTestCase nCases = do
    unless (nCases == 0) $ do
        getLine
        valsStr <- getLine
        let vals = map (read :: String -> Int) $ words valsStr
        print $ invCount vals
        processTestCase $ nCases - 1

main :: IO()
main = do
    nCasesStr <- getLine
    let nCases = read nCasesStr :: Int
    processTestCase nCases
