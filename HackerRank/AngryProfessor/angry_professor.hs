import Control.Monad

wasClassCanceled :: [Int] -> Int -> String
wasClassCanceled arrivals thresh =
    if length validArrivals < thresh then "YES" else "NO"
    where validArrivals = filter (<=0) arrivals

processCase :: Int -> IO()
processCase nCases = do
    unless (nCases == 0) $ do
        specStr <- getLine
        arrivalsStr <- getLine
        
        let thresh = read (words specStr !! 1) :: Int
        let arrivals = map (read :: String -> Int) (words arrivalsStr)
        
        putStrLn $ wasClassCanceled arrivals thresh
        processCase $ nCases - 1


main :: IO()
main = do
    nCasesStr <- getLine
    let nCases = read nCasesStr :: Int
    processCase nCases
