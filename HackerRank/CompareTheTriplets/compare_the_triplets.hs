asIntList :: String -> [Int]
asIntList st = [read w :: Int | w <- (words st)]

calcCmpPts :: [Int] -> [Int] -> Int
calcCmpPts xs ys = sum (map fromEnum [x > y | (x, y) <- (zip xs ys)])

main :: IO()
main = do
    xsStr <- getLine
    ysStr <- getLine
    let xs = asIntList xsStr; ys = asIntList ysStr in
        let ptsA = calcCmpPts xs ys; ptsB = calcCmpPts ys xs in do
            putStrLn ((show ptsA) ++ " " ++ (show ptsB))