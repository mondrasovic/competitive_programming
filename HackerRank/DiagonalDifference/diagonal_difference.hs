import Control.Monad

asMatrix :: [String] -> [[Int]]
asMatrix rows = [[read x :: Int | x <- (words row)] | row <- rows]

mainDiagSum :: [[Int]] -> Int
mainDiagSum mtx = sum [row !! i | (i, row) <- zip [0..] mtx]

secondDiagSum :: [[Int]] -> Int
secondDiagSum mtx = sum [row !! i | (i, row) <- zip (reverse [0..(length mtx) - 1]) mtx]

main :: IO()
main = do
    n <- getLine
    rows <- replicateM (read n) getLine
    let mtx = asMatrix rows in do
        putStrLn (show (abs ((mainDiagSum mtx) - (secondDiagSum mtx))))
