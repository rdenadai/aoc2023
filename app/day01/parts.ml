open Support.Utils

let file = "day01/input.txt"
let char_to_string (c : char) = String.make 1 c

let is_digit (c : char) =
  match c with '0' .. '9' -> char_to_string c | _ -> ""

let concat_first_last (lst : string list) =
  match List.filter (( <> ) "") lst with
  | [] -> "0"
  | [ x ] -> x ^ x
  | first :: rest ->
      let rec last_element l =
        match l with
        | [ x ] -> x
        | _ :: t -> last_element t
        | [] -> failwith "0"
      in
      first ^ last_element rest

let parse_line (line : string) =
  String.split_on_char ' ' line
  |> List.map (fun s ->
         String.to_seq s |> List.of_seq |> List.map is_digit
         |> concat_first_last)
  |> List.map int_of_string

let sum (lst : int list) = List.fold_left ( + ) 0 lst

let _compute (lines : string list) =
  List.map parse_line lines |> List.flatten |> sum

let () =
  let lines = read_lines file in
  _compute lines |> string_of_int |> print_endline
