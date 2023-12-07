open Support.Utils

let file = "day06/input.txt"


let rec zip lst1 lst2 = 
  match lst1, lst2 with
  | x::xs, y::ys -> (x, y) :: zip xs ys
  | _ -> []

let rec range start finish =
  if start > finish then []
  else start :: range (start + 1) finish
;;

let parse_line_to_num (line: string) (clear_str: string) =
  Str.(global_replace (Str.regexp clear_str) "" line) 
  |> String.split_on_char ' ' 
  |> List.filter ((<>) "") 
  |> List.map int_of_string
;;

let parser_part_1 (lines: string list) = 
  match lines with
  | [time; distance] ->
    let t = parse_line_to_num time "Time: " in
    let d = parse_line_to_num distance "Distance: " in
    zip t d
  | _ -> failwith "Invalid input"
;;

let _compute (lines: string list) = 
  parser_part_1 lines
  |> List.map (fun (t, d) -> 
    range 0 t
    |> List.fold_left (
      fun acc c -> if ((t - c) * c > d) then acc + 1 else acc
    ) 0
  )
;;

let () = 
  let lines = read_lines file in
  let result = _compute lines
  |> List.fold_left (fun acc cur -> acc * cur) 1 in
  string_of_int result |> print_endline;
  assert (result == 288)
;;
