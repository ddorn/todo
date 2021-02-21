{
  description = "Booking website";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs?ref=nixpkgs-unstable";
  };

  outputs = { self, nixpkgs }: let
    system = "x86_64-linux";
  in
  with nixpkgs.legacyPackages.${system};
  let
    pythonEnv = python38.withPackages(ps: with ps; [
      fastapi
      uvicorn
    ]);
  in
  {
    devShell.${system} = mkShell {
      buildInputs = [
        nodejs
        nodePackages.npm
        pythonEnv
      ];

      PYTHONPATH = "website";
      PORT = "8300";

      shellHook = ''
      function start() {
        if [ "$1" != "dev" ]
        then
          uvicorn website.main:app --port $PORT
        else
          DEV=true uvicorn website.main:app --port $PORT --reload
        fi
      }
      '';
    };
  };
}
