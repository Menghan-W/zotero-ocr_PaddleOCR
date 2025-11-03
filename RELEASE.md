# Release Process Guide

This document explains how to create releases for the Zotero OCR PaddleOCR plugin using GitHub Actions.

## Automated Release Workflows

This repository has two GitHub Actions workflows for creating releases:

### 1. Automatic Release (Tag-based)

**Workflow file:** `.github/workflows/release.yml`

This workflow automatically creates a release when you push a version tag.

**How to use:**

```bash
# Make sure all your changes are committed
git add .
git commit -m "Prepare for release"

# Create and push a version tag
git tag v1.0.1
git push origin v1.0.1
```

**What happens:**
1. The workflow detects the new tag
2. Builds the XPI package
3. Generates release notes from commits
4. Creates a GitHub release with the XPI attached
5. Updates `updates.json` with the new version information

### 2. Manual Release (Workflow Dispatch)

**Workflow file:** `.github/workflows/manual-release.yml`

This workflow can be triggered manually from the GitHub Actions tab, useful for testing or when you want more control.

**How to use:**

1. Go to the "Actions" tab in your GitHub repository
2. Select "Manual Release" from the workflows list
3. Click "Run workflow"
4. Enter the version number (e.g., `1.0.1`)
5. Optionally mark as pre-release
6. Click "Run workflow" button

**What happens:**
1. Validates the version format
2. Updates version in `manifest.json`, `pixi.toml`, and optionally `install.rdf`
3. Builds the XPI package
4. Commits version changes
5. Creates and pushes a version tag
6. Creates a GitHub release with the XPI attached
7. Updates `updates.json`

## Version Numbering

Use [Semantic Versioning](https://semver.org/):
- `X.Y.Z` format (e.g., `1.0.1`)
- **X** (Major): Incompatible API changes
- **Y** (Minor): New functionality, backwards compatible
- **Z** (Patch): Bug fixes, backwards compatible

## Release Checklist

Before creating a release:

- [ ] Update CHANGES.md with new version notes
- [ ] Test the plugin thoroughly
- [ ] Update documentation if needed
- [ ] Ensure all tests pass
- [ ] Commit all changes
- [ ] Choose appropriate version number

## Release Notes

Release notes are automatically generated from:
- Git commit messages since the last tag
- Installation instructions
- Links to documentation

To improve release notes, write clear commit messages:
- ✅ `Add support for Japanese OCR`
- ✅ `Fix PDF generation error`
- ❌ `update`
- ❌ `fix bug`

## Troubleshooting

### "Tag already exists"
```bash
# Delete the tag locally and remotely
git tag -d v1.0.1
git push origin :refs/tags/v1.0.1

# Then create it again
git tag v1.0.1
git push origin v1.0.1
```

### "Workflow failed"
1. Check the Actions tab for error details
2. Common issues:
   - Version format incorrect (must be X.Y.Z)
   - Build script failed (check `build.sh`)
   - Permission issues (check repository settings → Actions → General → Workflow permissions)

### "Release not appearing"
- Ensure "Workflow permissions" in repository settings allows "Read and write permissions"
- Check that `GITHUB_TOKEN` has necessary permissions

## Manual Release (Without GitHub Actions)

If you prefer to create releases manually:

```bash
# 1. Update version
VERSION="1.0.1"
perl -pi -e "s/\"version\": \"[^\"]*\"/\"version\": \"$VERSION\"/" src/manifest.json
perl -pi -e "s/^version = \"[^\"]*\"/version = \"$VERSION\"/" pixi.toml

# 2. Build
./build.sh $VERSION

# 3. Commit and tag
git add src/manifest.json pixi.toml
git commit -m "Release v$VERSION"
git tag -a "v$VERSION" -m "Release v$VERSION"
git push origin main
git push origin "v$VERSION"

# 4. Create release on GitHub
# - Go to Releases → Draft a new release
# - Choose the tag you created
# - Upload build/zotero-ocr-$VERSION.xpi
# - Write release notes
# - Publish
```

## Configuration

### Workflow Permissions

Make sure your repository has the correct permissions:

1. Go to Settings → Actions → General
2. Under "Workflow permissions", select:
   - ✅ "Read and write permissions"
   - ✅ "Allow GitHub Actions to create and approve pull requests"

### Branch Protection

If your main branch has protection rules:
- The workflow will need permission to push commits
- Consider using a bot account or personal access token

## Examples

### Example 1: Bug Fix Release

```bash
# Fix a bug
git add src/zotero-ocr.js
git commit -m "Fix PDF generation error for files with special characters"

# Create patch release
git tag v1.0.1
git push origin v1.0.1

# GitHub Actions automatically creates the release
```

### Example 2: Feature Release

```bash
# Add new feature
git add src/
git commit -m "Add support for Korean language OCR"

# Update documentation
git add README.md
git commit -m "Update documentation for Korean support"

# Create minor release
git tag v1.1.0
git push origin v1.1.0
```

### Example 3: Manual Pre-release

1. Go to Actions → Manual Release
2. Version: `2.0.0-beta.1`
3. Check "Mark as pre-release"
4. Run workflow

## Best Practices

1. **Test before release**: Always test the XPI package locally before creating a release
2. **Clear commit messages**: Write descriptive commits for better release notes
3. **Update CHANGES.md**: Keep the changelog up to date
4. **Semantic versioning**: Follow semver for version numbers
5. **Tag format**: Always use `vX.Y.Z` format (with 'v' prefix)
6. **Release cadence**: Consider a regular release schedule (e.g., monthly)

## Support

For issues with the release process:
- Check the [Actions tab](https://github.com/Menghan-W/zotero-ocr_PaddleOCR/actions) for workflow runs
- Review workflow logs for detailed error messages
- Open an issue if you need help
