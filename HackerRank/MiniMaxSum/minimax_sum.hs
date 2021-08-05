calcSum :: [Int] -> (Int -> Int -> Int) -> Int -> Int -> Int
calcSum _      _ s 0 = s
calcSum (x:xs) f s n
    | n == (length xs + 1) = withVal
    | otherwise            = f withVal withoutVal
        where withVal    = calcSum xs f (s + x) (n - 1)
              withoutVal = calcSum xs f s n

main :: IO()
main = do
    xsStr <- getLine
    let xs = map (read :: String -> Int) $ words xsStr in do
        putStrLn ((show $ calcSum xs min 0 4) ++ " " ++ (show $ calcSum xs max 0 4))
