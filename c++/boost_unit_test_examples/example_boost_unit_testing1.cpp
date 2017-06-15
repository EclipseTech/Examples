// Example compile $<compiler> <thisFileName> -lboost_unit_test_framework

// Needed for dynamic linking
#define BOOST_TEST_DYN_LINK
// This could be used to define this as the main test module instead of a named module
//#define BOOST_TEST_MAIN
// Define test suite module name as "test something"
#define BOOST_TEST_MODULE "Example boost unit testing 1"
#include <boost/test/unit_test.hpp>
// Use #include <boost/test/included/unit_test.hpp> for static linking

// Setup and teardown fictures
#include <iostream>
struct F
{
    F() { std::cout << "setup 1" << std::endl; }
    ~F() { std::cout << "teardown 1" << std::endl; }
};
// Define F as global fixture, going to leave commented out for less output for now
//BOOST_GLOBAL_FIXTURE( F );

// Example successful unit tests
// automatic test case registration
BOOST_AUTO_TEST_CASE( test1 )
{
    BOOST_CHECK( 1 == 1 );
    BOOST_CHECK( 1 == 2 );
    BOOST_CHECK( 1 == 3 );
}

struct F2
{
    F2() { std::cout << "setup 2" << std::endl; }
    ~F2() { std::cout << "teardown 2" << std::endl; }
};
// Example failure unit test
// each test file may contain any number of test cases; each test case has to have unique name
// Define F2 as local test fixture
BOOST_FIXTURE_TEST_CASE( test2, F2 )
{
    int i = 1;
    BOOST_CHECK_EQUAL( i, 1 );
    // Failure here means entire "test2" is a failure
    // Each BOOST_AUTO_TEST_CASE is considered an individual test
    //  each check within the test is not part of the overall test
    BOOST_CHECK_EQUAL( i, 2 );
}
