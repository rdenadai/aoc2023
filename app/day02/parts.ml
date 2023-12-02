open Support.Utils

let file = "day02/input.txt"

let regexes: (string, Str.regexp) Hashtbl.t = Hashtbl.create 3;;
Hashtbl.add regexes "red" (Str.regexp "\\([0-9]+ red\\)");;
Hashtbl.add regexes "green" (Str.regexp "\\([0-9]+ green\\)");;
Hashtbl.add regexes "blue" (Str.regexp "\\([0-9]+ blue\\)");;

let check_for_games_with: (string, int) Hashtbl.t = Hashtbl.create 3;;
Hashtbl.add check_for_games_with "red" (12);;
Hashtbl.add check_for_games_with "green" (13);;
Hashtbl.add check_for_games_with "blue" (14);;

let rec last_element (element: string list) = 
  match element with
  | [last] -> last
  | _ :: tail -> last_element tail
  | _ -> failwith "Invalid input"

let find_all regex s =
  let rec find acc pos =
    try
      let _ = Str.search_forward regex s pos in
      let match_str = Str.matched_string s in
      find (match_str :: acc) (Str.match_end ())
    with Not_found -> List.rev acc
  in
  find [] 0
;;

let game (item: string list) =
  match item with
  | [game; bags] -> 
    let exists = List.for_all (fun (color, regex) -> 
      find_all regex bags
      |> List.for_all (fun item -> 
        let v = String.split_on_char ' ' item |> List.hd |> int_of_string in
        let max = Hashtbl.find check_for_games_with color in
        v <= max
      )
    ) (Hashtbl.to_seq regexes |> List.of_seq) in
    
    if exists then
      String.split_on_char ' ' game |> last_element |> int_of_string
    else 0
  | _ -> failwith "Invalid input"
;;

let parse_line (line: string) = 
  String.split_on_char ':' line 
  |> game 
;;

let _compute (lines: string list) = 
  List.map parse_line lines 
  |> List.fold_left (+) 0
;;

let () = 
  let lines = read_lines file in
  _compute lines |> string_of_int |> print_endline;
;;
