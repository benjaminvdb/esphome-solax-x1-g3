# Contributing

Thanks for helping! Every kind of contribution is welcome, including "this step confused me".

- **Questions and problems:** open an
  [issue](https://github.com/benjaminvdb/solax-esphome/issues/new/choose). The form asks
  for the details needed to help: inverter model, serial number prefix, firmware version,
  RS485 module and a log.
- **It works on your inverter?** Tell us in an issue which model and firmware, so it can
  be added to the list in the README.
- **Changes to the configuration:** test them on a real inverter, run *Validate* in
  ESPHome Builder (or `esphome config solax-x1.yaml`), and describe what you tested in the
  pull request.
- **Changes to the wiring diagram:** edit `diagrams/wiring.py` and run
  `python diagrams/wiring.py`. Commit the script and `images/wiring.svg` together.
- **Writing style:** short sentences, plain words, and explain every technical term the
  first time it appears (or add it to `docs/glossary.md`). After each step, say what the
  reader should see when it worked.
