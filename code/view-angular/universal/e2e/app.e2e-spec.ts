import { UniversalPage } from './app.po';

describe('universal App', () => {
  let page: UniversalPage;

  beforeEach(() => {
    page = new UniversalPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});
