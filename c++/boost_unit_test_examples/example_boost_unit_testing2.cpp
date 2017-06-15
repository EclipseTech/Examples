// Takes a long time to compile with the included lib
#include <boost/test/included/unit_test.hpp>
using namespace boost::unit_test;

int return_one()
{
    return 1;
}

// Need to register unit test function
void test_something()
{
    BOOST_CHECK_EQUAL(return_one(), 2);
    BOOST_REQUIRE_EQUAL(return_one(), 2);
}

test_suite* init_unit_test_suite( int, char* [] )
{
    // Test suite name
    framework::master_test_suite().p_name.value = "Example boost unit testing 2";

    // Register test_something
    // optional: # of expected failing tests
    framework::master_test_suite().add( BOOST_TEST_CASE( &test_something ), 0 );

    return 0;
}
