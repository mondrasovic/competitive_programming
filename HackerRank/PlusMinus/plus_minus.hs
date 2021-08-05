import Numeric

cmpRatio cmps c = (fromIntegral $ length $ filter (==c) cmps) / (fromIntegral $ length cmps)

calcNumRatios xs = cmpRatio cmps LT:cmpRatio cmps GT:cmpRatio cmps EQ:[]
    where cmps = map (compare 0) xs

concatFloats :: [Float] -> Int -> String -> String
concatFloats [] d s = ""
concatFloats (x:[]) d s = showFFloat (Just d) x ""
concatFloats (x:xs) d s = (concatFloats [x] d s) ++ s ++ (concatFloats xs d s)

main :: IO()
main = do
    getLine
    vals <- getLine
    let xs = map (read :: String -> Int) (words vals) in do
        putStrLn (concatFloats (calcNumRatios xs) 6 "\n")

