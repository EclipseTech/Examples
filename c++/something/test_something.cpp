#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE "test something"
#include <boost/test/unit_test.hpp>

#include <fstream>
#include <iostream>
#include <string>
class Something
{
    //const char * filename;
    public:
        std::string read_first_line_in_file(const char * filename);
};
std::string Something::read_first_line_in_file(const char * filename)
{
    //this->filename = filename;
    std::ifstream inputfile( filename );
    std::string line;
    std::getline( inputfile, line );
    inputfile.close();

    return line;
}

BOOST_AUTO_TEST_CASE( test_read_first_line_in_file )
{
    Something first;
    std::string input = first.read_first_line_in_file( "input.txt" );
    BOOST_CHECK_EQUAL(input, "input");
}
