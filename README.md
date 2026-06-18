# Ishan Shah Personal Website

Static GitHub Pages portfolio site for Ishan Shah, Staff Software Engineer.

Canonical placeholder domain:

```text
https://ishandshah.github.io
```

If a custom domain is added later, update canonical URLs, Open Graph URLs, Twitter image URLs, JSON-LD URLs, `sitemap.xml`, and `robots.txt`.

## Folder Structure

```text
portfolio/
├── index.html
├── about.html
├── projects.html
├── leadership.html
├── speaking.html
├── service.html
├── resume.html
├── contact.html
├── robots.txt
├── sitemap.xml
├── assets/
│   ├── Ishan_Shah_Resume.pdf
│   ├── og-image.png
│   ├── profile.jpg
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── main.js
│   └── resume/
│       └── Ishan-Shah-Resume.pdf
└── README.md
```

## Local Preview

Run a small static server:

```bash
python3 -m http.server 8081
```

Then visit:

```text
http://localhost:8081
```

## GitHub Pages Deployment

1. Create or open the GitHub repository.
2. Commit and push the contents of this folder to the repository root.
3. In GitHub, go to `Settings` -> `Pages`.
4. Under `Build and deployment`, select `Deploy from a branch`.
5. Choose the `main` branch and `/root`.
6. Save. GitHub will publish the site after the Pages workflow completes.

Expected site URL:

```text
https://ishandshah.github.io/portfolio/
```

For GitHub Pages to use this path, the repository must be named `portfolio` or the site must be published from a repository with that name.

If you want the site at `https://ishandshah.github.io/`, publish it from a repository named `ishandshah.github.io`.

## Placeholder Links To Replace

Search for these values before moving to a custom domain:

```text
https://ishandshah.github.io
```

The LinkedIn URL is currently:

```text
https://www.linkedin.com/in/ishandshah/
```

The GitHub profile URL is currently:

```text
https://github.com/ishandshah
```

## Indexing Checklist

1. Publish the site on GitHub Pages.
2. Confirm the site loads at the final GitHub Pages URL.
3. Confirm these files load:
   - `/robots.txt`
   - `/sitemap.xml`
4. Add the site to Google Search Console.
5. Submit `sitemap.xml` in Google Search Console.
6. Use URL Inspection for the homepage and request indexing.
7. Check that canonical URLs match the live domain.
8. Update LinkedIn and GitHub profile links to point to the website.
9. Add the website link to the resume PDF.
10. If a custom domain is added later, update canonical URLs, `sitemap.xml`, `robots.txt`, Open Graph URLs, and structured data.

Optionally submit the site to Bing Webmaster Tools and submit the same `sitemap.xml`.

## Validation Tools

- Google Rich Results Test for JSON-LD structured data.
- Google Search Console URL Inspection.
- Lighthouse SEO and Accessibility checks.
- Open Graph preview testing.
- Live `robots.txt` check.
- Live `sitemap.xml` check.

## Notes

- The site is intentionally static and dependency-free for straightforward GitHub Pages hosting.
- Copy is public-safe and avoids confidential company details.
- The JavaScript only handles theme toggling and mobile navigation.
