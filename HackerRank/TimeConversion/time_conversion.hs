import Text.Printf

substr :: String -> Int -> Int -> String
substr s a b = take (b - a) (drop a s)

convertHours12To24 :: String -> Char -> String
convertHours12To24 hh pt = printf "%02d" (if pt == 'P' then hh' + 12 else hh')
    where hh' = (read hh :: Int) `mod` 12

convertTime :: String -> String
convertTime t =
    let hh = substr t 0 2
        mmss = substr t 2 8
        pt = t !! 8
    in (convertHours12To24 hh pt) ++ mmss

main = do
    t <- getLine
    putStrLn $ convertTime t
