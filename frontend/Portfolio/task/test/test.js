const path = require('path');
const pagePath = 'file://' + path.resolve(__dirname, '../src/index.html');
const {StageTest, correct, wrong} = require('hs-test-web');

class PortfolioTest extends StageTest {

    page = this.getPage(pagePath)

    tests = [
        this.page.execute(() => {
            let headings1 = document.getElementsByTagName('h1');

            if (headings1 === null || headings1.length === 0) {
                return wrong('Can\'t find the h1 element. Check that you created it.');
            }

            let header = headings1[0]
            let title = header.textContent || header.innerText;

            if (!title || title.length === 0) {
                return wrong('Can\'t find the text inside the h1 element.');
            }

            return correct();
        }),
        this.page.execute(() => {
            let headings2 = document.getElementsByTagName('h2');

            if (headings2 === null || headings2.length < 2) {
                return wrong(`Can't find two h2 elements. Your web page should have at least two h2 elements at this stage. There are only ${headings2.length}.`);
            }

            let found_about_me = false;
            let found_portfolio = false;

            for (let header of headings2) {
                let title = (header.textContent || header.innerText).trim();

                if (title && title.toLowerCase() === 'portfolio') {
                    found_portfolio = true;
                }

                if (title && title.toLowerCase() === 'about me') {
                    found_about_me = true;
                }
            }

            if (!found_about_me) {
                return wrong('Can\'t find "About me" text in one of the h2 elements.');
            }

            if (!found_portfolio) {
                return wrong('Can\'t find "Portfolio" text in one of the h2 elements.');
            }

            return correct();
        }),
        this.page.execute(() => {
            let images = document.getElementsByTagName('img');

            if (images === null || images.length < 2) {
                return wrong('Cannot find at least two img elements on your web page. Add one image that will represent you and at least one that will represent your work.');
            }

            return correct();
        }),
        this.page.execute(() => {
            let paragraphs = document.getElementsByTagName('p');

            if (paragraphs === null || paragraphs.length < 1) {
                return wrong('Cannot find at least one <p> element on your web page.');
            }

            return correct();
        })
    ]
}

it('Test stage', async function () {
    try {
        this.timeout(30000)
    } catch (ignored) {
    }
    await new PortfolioTest().runTests()
}, 30000)
