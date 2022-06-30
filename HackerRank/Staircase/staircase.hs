repeatChar :: Char -> Int -> String
repeatChar _ 0 = ""
repeatChar c n = c:repeatChar c (n - 1)

buildStaircaseRow :: Int -> Int -> String
buildStaircaseRow n size = (repeatChar ' ' (size - n)) ++ (repeatChar '#' n)

buildStaircase :: Int -> [String]
buildStaircase size = [buildStaircaseRow n size | n <- [1..size]]

main :: IO()
main = do
    n <- getLine
    mapM_ putStrLn $ buildStaircase (read n)
