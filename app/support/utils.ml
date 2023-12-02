let read_lines filename =
  let project_root = Sys.getcwd () in
  let absolute_path = (project_root ^ "/app/" ^ filename) in
  print_endline ("Reading file: " ^ absolute_path);
  let ic = open_in absolute_path in
  let rec read_lines_helper acc =
    match input_line ic with
    | line -> read_lines_helper (line :: acc)
    | exception End_of_file -> close_in_noerr ic; List.rev acc
  in
  read_lines_helper []
;;