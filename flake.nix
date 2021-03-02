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
      sqlalchemy
      alembic
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

      PYTHONPATH = "backend";
      PORT = "8300";

      shellHook = ''
      function start() {
        if [ "$1" != "dev" ]
        then
          uvicorn backend.main:app --port $PORT
        else
          DEV=true uvicorn backend.main:app --port $PORT --reload
        fi
      }
      '';
    };
  };
}
