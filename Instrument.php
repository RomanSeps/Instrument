<?php
abstract class Instrument{
    private $name;
    abstract function setter($name);
    abstract function getter($name);
}

class String_instrument extends Instrument{
    private $num_of_strings;
    abstract function setter($num_of_strings);
    abstract function getter($num_of_strings);
}

$v = new String_instrument("Violin", 4);
