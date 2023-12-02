open Support.Utils

let file = "day01/input.txt"

let parse_line (line: string) = 
  String.split_on_char ' ' line
;;

let _compute (lines: string list) = 
  List.map parse_line lines
;;

let () = 
  let lines = read_lines file in
  let _ = _compute lines in
  print_endline "Not Implemented"
;;