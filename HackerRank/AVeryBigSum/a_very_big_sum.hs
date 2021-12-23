main :: IO()
main = do
    getLine
    xsStr <- getLine
    putStrLn (show (sum [read w :: Integer | w <- (words xsStr)]))
